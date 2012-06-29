/* Author: Unomena */

$(document).ready(function(){
	
	var standard_arguments = {
			target : '#cboxLoadedContent',
			beforeSubmit : function(){ 
								$('#popup_overlay').show(); 
								$('#popup_overlay_loading').show();
							},
			success : function(){ $.colorbox.resize(); },
			clearForm : 'true'
			}

	$('#frmRegister').ajaxForm(standard_arguments);
	$('#frmSpeaker').ajaxForm(standard_arguments);
	
});