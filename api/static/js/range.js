export function set_in_range(parent) {
 var in_range = false;
 $(".range_parent > tbody > tr > td > table").each(function() {
   console.log("class", $(this).attr("class"), $(this).parents().length);
   if ($(this).hasClass("range_start") || $(this).hasClass("range_end")) {
     in_range = $(this).hasClass("range_start");
     $(this).removeClass("range_start").removeClass("range_end").addClass("range_included");
   } else if (in_range) {
     $(this).addClass("range_included");
   }
 });
}

export function clean_range() {
 $(".range_parent").removeClass("range_parent");
 $(".range_included").removeClass("range_included");
}

export function send_merge() {
  console.log("range_parent", $(".range_parent").attr("id"));
}
