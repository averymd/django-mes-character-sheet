$(function() {
	$(".priority-row").sortable({ appendTo: document.body, helper: "clone", cursor: "move" }); 
	$(".priority-row").disableSelection();
});