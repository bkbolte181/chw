$(document).ready(function() {
	main_view();
});

$(".calendar-item").mouseover(function() {
	$(this).addClass("highlight-div");
});

$(".calendar-item").mouseleave(function() {
	$(this).removeClass("highlight-div");
});

function main_view() {
	$(".section").hide();
	$(".calendar-div").show();
	window.location.href = "#";
}

function list_events() {
	$(".section").hide();
	$(".all-items-div").show();
	window.location.href = "#allitems";
}

function open_item(dmy) {
	day = dmy.substring(0,2);
	month = dmy.substring(2,4);
	year = dmy.substring(4,8);
	$(".section").hide();
	$(".add-item-div").show();
	window.location.href = "#" + day + "-" + month + "-" + year
	var ajaxurl = $(".url-for-ajax").html();
	// $("#event-info").html(ajaxurl + " " + day + " " + month + " " + year);
		
	// Get the information for this date from the server
	$.ajax({
		type: "POST",
		url: ajaxurl,
		data: {
			csrfmiddlewaretoken: $('.csrf-token').html(),
			day: day,
			month: month,
			year: year,
		},
		success: function(data) {
			// Information about the date
			var date_info = "Date: " + data.date;
			$("#date-info").html(date_info);
			
			// Events
			var date_events_info = "";
			$("#date-events-info").html(date_events_info);
		},
	});
}

function save_item(id) {
	main_view();
}