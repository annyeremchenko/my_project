firstnameToChange = false;
$(document).ready(function() {
    $("#firstname").click(function(){
        alert("clicked");
        btn = $(this);
        if (!firstnameToChange){
            parent = btn.parent().children('span:first');
            alert(parent.text());
            parent.html('<input placeholder="' + '" name="firstname">');
            btn.text('Change');
            firstnameToChange = true;
        } else {
            parent = btn.parent().children('span:first');
            alert(parent.children('input:first').val());
        }
    });
});