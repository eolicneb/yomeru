(function(old) {
  $.fn.attr = function() {
    if(arguments.length === 0) {
      if(this.length === 0) {
        return null;
      }

      var obj = {};
      $.each(this[0].attributes, function() {
        if(this.specified) {
          obj[this.name] = this.value;
        }
      });
      return obj;
    }

    return old.apply(this, arguments);
  };
})($.fn.attr);


$.fn.deepest = function(selector) {
	var $target = $(this).children(selector);
	while( $target.length ) {
	  $target = $target.children(selector);
	}
	return $target.end();
};


wipeClass = function(class_name) {
    var class_selector = "." + class_name;
    $(".bun").find(class_selector).removeClass(class_name);
};
//import {set_in_range, clean_range} from './range.js';

var STATE = {SELECTED: "state_selected",
             RANGE: "state_range",
             CLEAN: "clean"}

var button_pressed = false;
var state = STATE.CLEAN;

// RANGE methods:
function set_in_range(parent) {
 var in_range = false;
 $(".range_parent > tbody > tr > td > table").each(function() {
   if ($(this).hasClass("range_start") || $(this).hasClass("range_end")) {
     in_range = $(this).hasClass("range_start");
     $(this).addClass("range_included");
   } else if (in_range) {
     $(this).addClass("range_included");
   }
 });
}


function clean_range() {
  ["range_parent", "range_included", "range_start", "range_end"].forEach(wipeClass);
}


function set_new_range(parent, new_range_string) {
  var new_range = $.parseHTML(new_range_string);
  var replace = $(new_range).find("#" + parent.attr("id"));
  parent.replaceWith(replace);
}


function perform_merge() {
  var $selected = $(".range_parent").length? $(".range_parent") : $(".deepest_selected");
  var range_data = {
    "parent_id": $selected.attr("id"),
    "range": $(".range_included").map(function(ix, el) { return $(el).attr("id"); }).toArray(),
    "imi": $("#merge_form [name='new_imi']").val(),
    "onsei": $("#merge_form [name='new_onsei']").val()
  }
  console.log("range_data:", range_data);
  $.ajax({
    url: "http://127.0.0.1:5000/merge",
    type: "POST",
    contentType: "application/json",
    data: JSON.stringify(range_data),
    success: function(result) {
        set_new_range($selected, result);
        $selected.focus();
    },
    complete: function() {
      clean_range();
      bind_all();
    }
  });
}

view_kao = function(selector) {
  $("#merge_form [name='new_onsei']").val(null);
  var imi_selector = selector + " .imi";
  $("#merge_form [name='new_imi']").val($(imi_selector).length==1 ? $(imi_selector).text() : $(imi_selector).last().text());
  $("#range_kao").text($(selector + " .kao").text());
};
// END RANGE methods

// SELECTED methods
function clean_selected() {
  ["selected", "deepest_selected"].forEach(wipeClass);
}


function perform_unwrap() {
    var $selected = $(".deepest_selected");
    var $parent = $selected.parents("table").first();
    var unwrap_data = {wrapped_id: $selected.attr("id"),
                       parent_id: $parent.attr("id")};
    $.ajax({
        url: "http://127.0.0.1:5000/unwrap",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify(unwrap_data),
        success: function(result) {
            set_new_range($parent, result);
            $parent.focus();
        },
        complete: function() {
            clean_selected();
            bind_all();
        }
    });
}
// END SELECTED methods


function clean_pressed() {
   ["pressed", "left", "stepped"].forEach(wipeClass);
}


function bind_all() {
 $(".kao").css({userSelect: 'none'});
 $(".onsei").css({userSelect: 'none'});
 $(".imi").css({userSelect: 'none'});

 $(".bun td").click(function(event, ){
   clean_pressed();
   if ($(".selected").length) {
       $(".selected").last().addClass("deepest_selected");
       wipeClass("selected");
       console.log($(".deepest_selected").text());
       view_kao(".deepest_selected")
   }
 });

 $("table").mousedown(function(){
   clean_range();
   button_pressed = true;

   $(this).addClass("pressed");

   wipeClass("deepest_selected");
   $(this).addClass("selected");
 });

 $("table").mouseleave(function() {
   if (button_pressed === false) { return; }

   if ($(this).hasClass("pressed")) {
     $(this).addClass("left");
   } else {
     $(this).removeClass("stepped");
   }

   wipeClass("selected");
 });

 $("table").mouseenter(function() {
   if(button_pressed === false) { return; }
   if ($(this).hasClass("pressed")) {
     $(this).removeClass("left");
   } else {
     $(this).addClass("stepped");
   }
 });

 $("table").mouseup(function(){
   button_pressed = false;
   $("table.left").first().parents("table").not(".left").first().addClass("range_parent");
   $(".range_parent").find("table.left").first().removeClass().addClass("range_start");
   $(".range_parent").find("table.stepped").first().removeClass().addClass("range_end");
   set_in_range($(".range_parent"));
   view_kao(".range_included");
   clean_pressed();
 });
}


$(document).ready(function() {
 $("#merge_form").submit(function(e){
   perform_merge();
   e.preventDefault();
 });
 bind_all();
});
