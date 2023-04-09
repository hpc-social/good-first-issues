$('#bootstrapForm').submit(function (event) {
    event.preventDefault()
    var extraData = {}
    {
    /* Parsing input date id=1751423871 */
    var dateField = $("#1751423871_date").val()
    var timeField = $("#1751423871_time").val()
    let d = new Date(dateField)
    if (!isNaN(d.getTime())) {
        extraData["entry.1751423871_year"] = d.getFullYear()
        extraData["entry.1751423871_month"] = d.getMonth() + 1
        extraData["entry.1751423871_day"] = d.getUTCDate()
    }
    if (timeField && timeField.split(':').length >= 2) {
        let values = timeField.split(':')
        extraData["entry.1751423871_hour"] = values[0]
        extraData["entry.1751423871_minute"] = values[1]
    }
    }
    $('#bootstrapForm').ajaxSubmit({
    data: extraData,
    dataType: 'jsonp',  // This won't really work. It's just to use a GET instead of a POST to allow cookies from different domain.
    error: function () {
        // Submit of form should be successful but JSONP callback will fail because Google Forms
        // does not support it, so this is handled as a failure.
        alert('Form Submitted. Thanks.')
        // You can also redirect the user to a custom thank-you page:
        // window.location = 'http://www.mydomain.com/thankyoupage.html'
    }
    })
})

function toggleNightMode(){
	if(document.documentElement.getAttribute('data-theme') == 'light'){
		document.documentElement.setAttribute('data-theme', 'dark');
		document.getElementById('mode-switcher').classList.add('active');
		localStorage.setItem("theme","dark");
	}
	else{
		document.documentElement.setAttribute('data-theme', 'light');
		document.getElementById('mode-switcher').classList.remove('active');
		localStorage.setItem("theme","");
	}
}

