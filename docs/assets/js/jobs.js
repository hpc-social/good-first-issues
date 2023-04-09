//Initialize table for jobs
$('.jobs-table').DataTable( {
     order: [[ 1, "asc" ]], //set date column as default order, earliest to latest
     lengthMenu: [ 20, 50, 100 ], //options for entry control
     dom: '<"search-wrap"f<"dropfilters">><"top" l<"clear">><"bottom" tipl>', //https://datatables.net/examples/basic_init/dom.html
     language: {
      emptyTable:     "There are no jobs available at this time",
      search: "Search by keyword",
      zeroRecords: "No jobs match your search criteria. Try again or clear the search to start over.",
      info: "Showing _START_ to _END_ • _TOTAL_",
      lengthMenu:     "Show _MENU_ jobs",
    }    
} );


$(document).ready(function() {
  var dropfilters = $("#filter-wrapper").html();
  var placement = document.querySelector(".dropfilters");
  $(placement).append(dropfilters);
  
  var cleartoggle = $("#clear").html();
  var placementb = document.querySelector(".clear");
  $(placementb).append(cleartoggle);

  // Hide second length picker
  $($('.dataTables_length')[1]).hide()

});


$(document).ready(function() {
   var table =  $('.jobs-table').DataTable();

    // Jobs type is in row 1, locations in 2
    $('#repository-filter').on('change', function () {
      table.columns(1).search(this.value).draw();
    });
    $('#tags-filter').on('change', function () {
      table.columns(2).search( this.value ).draw();
    });
    $('#posted-by-filter').on('change', function () {
      table.columns(3).search( this.value ).draw();
    });  
});


//Clear all fields in the search
$(document).ready(function() {
  var table =  $('.jobs-table').DataTable();
$('#clear-all').click(function() {
    $('#DataTables_Table_0_filter input, .form-control').val("");
    table.search('').draw(); //required after
    table.columns(0).search("").draw();
    table.columns(1).search("").draw();
    table.columns(2).search("").draw();
    table.columns(3).search("").draw();
    table.columns(4).search("").draw();
    $.fn.dataTable.ext.search.pop();
    table.draw();
       
});
});

// Add background colors to filters that are not empty
$(document).ready(function() {
  $('#DataTables_Table_0_filter input, .form-control').on('keyup change input', 
   function(){
     var field = $( this );        
    if ( field.val() != '' ) {
        field.addClass('data-entered');
    } else {
        field.removeClass('data-entered');
    }
});
 $('#clear-all').on('click', 
   function(){
   $('#DataTables_Table_0_filter input, .form-control').removeClass('data-entered');
 });
 
});

// Set clear on the datpicker clear button
$(document).on("click", ".clear-date-only", function(){ // if they click clear
  var table =  $('.jobs-table').DataTable();
  var inputs =  $('#DataTables_Table_0_filter input, .form-control');
    $('#min').val("");
    $.fn.dataTable.ext.search.pop();
    table.draw();
    inputs.removeClass('data-entered');
});

// Set clear on the timepicker button
$(document).on("click", ".clear-time-only", function(){ // if they click clear
   var table =  $('.jobs-table').DataTable();
    var inputs =  $('#DataTables_Table_0_filter input, .form-control');
    $('.timepicker').val("");
    $('.ui-timepicker-select').val("");
    table.columns(2).search("").draw();
    inputs.removeClass('data-entered');
});
