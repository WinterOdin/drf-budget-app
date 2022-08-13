function runWallet(url_wallet, url_entry) {

    function parseWalletData(container_id, wallet_num, wallet_name, wallet_uuid, wallet_shared){
        var wallet_container = container_id;
        var wallet_num = parseInt(wallet_num)+1
        var wallet_instance = 
        '<div data_wallet="'+wallet_uuid+'"class="row row_wallet_instance"><div class="col-12">'+
        '<div class="wallet_instance_content"><span class="wallet_instance_num">'+wallet_num+
        '<span class="wallet_instance_dot">.</span>'+'</span>'+
        '<span class="wallet_instance_txt">'+wallet_name+'</span></div>'+
        '<div class="wallet_instance_uuid">ID: '+wallet_uuid+'</div>'+
        '<div class="wallet_instance_shared">'+wallet_shared+'</div>'+
        '</div></div>';
        wallet_container.insertAdjacentHTML('beforeend', wallet_instance);
    };

    function parseDetail(container_id, wallet_num, wallet_name, wallet_uuid, wallet_shared, wallet_date){
        info_container = container_id
        var wallet_num = parseInt(wallet_num)+1
        info_instance = 
        '<div id="'+wallet_uuid+'"class="info_instance_div"><div class="info_wallet_title">'+ wallet_name+'</div>'+
            '<div class="row"><div class="col-6"><span class="info_wallet_id">'+wallet_uuid+'</span></div>'+
                '<div class="col-6"><span class="info_wallet_date">'+wallet_date+'</span></div></div>'+'</div>'
            
        info_container.insertAdjacentHTML('beforeend', info_instance);   
    }

    function populateWallets() {
        $.ajax({
			type: 'GET',
			url: url_wallet,
			headers: {
				"X-Requested-With": "XMLHttpRequest",
			},
			success: function(response) {

                wallet_pos = document.getElementById('wallet_row');
                detail_pos = document.getElementById('dynamic_content');
                var counter = 0;
                //?
                var data = JSON.stringify(response)
                data = JSON.parse(data)
                
                console.log(data[0].id)
                if(Object.keys(data).length > 0){
                    for(var key in data){
                        if(data.hasOwnProperty(key)){
                            parseWalletData(wallet_pos, counter, data[counter].name, data[counter].id, data[counter].viewable)
                            parseDetail(detail_pos, counter, data[counter].name, data[counter].id, data[counter].viewable, data[counter].date_added)
                            counter += 1;
                        }
                    }
                }
            
                $(".row_wallet_instance").bind("click", function() {
                    $(".info_instance_div").fadeOut('fast');
                    var divId= $(this).attr("data_wallet");
                    $('#id_wallet_entry_id').val(divId);
                    setTimeout(function(){
                        $("#" + divId).fadeIn('fast')
                    }, 200);
                });
             
			},
			error: function(response) {
				
			}
	});}


    populateWallets()

	$("#budget_form").submit(function(e) {
		e.preventDefault();
		var serializedData = $(this).serialize();
        console.log(url_entry)
        console.log(serializedData)
		$.ajax({
			type: 'POST',
			url: url_entry,
			headers: {
				"X-Requested-With": "XMLHttpRequest",
			},
			data: serializedData,
			success: function(response) {
				console.log(response)
			
			},
			error: function(response) {
				console.log(response)
			}
		})
	})

	$(document).ajaxStart(function() {
		

	});


}