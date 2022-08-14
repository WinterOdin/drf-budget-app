function runWallet(url_wallet, url_entry) {
    
    function runWhistles(){
        var wallet_content_container = $("#dynamic_content")
        var wallet_instance_content = $("#wallet_row")
        
        wallet_content_container.fadeOut(100, function() {
            wallet_instance_content.empty()
        });

        wallet_instance_content.fadeOut(100, function() {
            wallet_content_container.empty();
                                populateWallets()
        setTimeout(function() {
            wallet_content_container.fadeIn('fast');
            wallet_instance_content.fadeIn('fast')
        }, 200);
        });
    }

    function parseWalletData(container_id, wallet_num, wallet_name, wallet_uuid){
        var wallet_container = container_id;
        var wallet_num = parseInt(wallet_num)+1
        var wallet_instance = 
        '<div data_wallet="'+wallet_uuid+'"class="row row_wallet_instance"><div class="col-12">'+
        '<div class="wallet_instance_content"><span class="wallet_instance_num">'+wallet_num+
        '<span class="wallet_instance_dot">.</span>'+'</span>'+
        '<span class="wallet_instance_txt">'+wallet_name+'</span></div>'+
        '<div class="wallet_instance_uuid">ID: '+wallet_uuid+'</div>'+
        '</div></div>';
        wallet_container.insertAdjacentHTML('beforeend', wallet_instance);
    };

    function parseDetail(container_id, wallet_num, wallet_name, wallet_uuid, 
        wallet_shared, wallet_date, entry, income_sum, expense_sum){
        
        info_container = container_id
        var wallet_num = parseInt(wallet_num)+1
        info_instance = 
        '<div id="'+wallet_uuid+'"class="info_instance_div"><div class="info_wallet_title">'+ wallet_name+'</div>'+
            '<div class="row">'+
            '<div class="col-sm-12 col-md-6">'+
            '<div class="info_wallet_pos"><div><span class="info_wallet_id">Wallet: '+wallet_uuid+'</span></div>'+
                '<div><span class="info_wallet_date">Date created: '+wallet_date+'</span></div>'+
                '<div class="info_wallet_shared">Shared with: '+wallet_shared+'</div></div></div>'+
                '<div class="col-sm-12 col-md-6">'+
                '<div class="chart">'+
                    '<canvas id="chart_'+wallet_uuid+'"</canvas>'+
                '</div></div></div>'+
                '<div class="info_wallet_entry">'+
                '<table class="table table-hover text-center" id="table_'+wallet_uuid+'">'+
                '<thead><tr>'+
                        '<th style="width: 30%">Title</th>'+
                        '<th style="width: 30%">Description</th>'+
                        '<th style="width: 10%">Amount</th>'+
                        '<th style="width: 15%">Type</th>'+
                        '<th style="width: 15%">Category</th>'+
                    '</tr>'+
                '</thead>'+
                '<tbody id="table-body"></tbody>'+
                '</table>'+
                '</div>'+'</div>'
        
        info_container.insertAdjacentHTML('beforeend', info_instance);  
        var table = document.getElementById('table_'+wallet_uuid)
        var ctx = document.getElementById('chart_'+wallet_uuid)
        
        const labels = ['expense', 'income']
        const colors = ['#480055', '#c1f7d3']
        var myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                datasets:[{
                    barPercentage: 0.5,
                    label: 'Income vs expense',
                    data: [income_sum, expense_sum],
                    backgroundColor: colors
                }],
            labels:labels
            },
            options:{
                responsive: false,
                maintainAspectRatio: false,
            }
        })
        

        for(i in entry){
            var row = `<tr>
                <td>${entry[i]['title']}</td>
                <td>${entry[i]['description']}</td>
                <td>${entry[i]['amount']}</td>
                <td>${entry[i]['entry_type']}</td>
                <td>${JSON.stringify(entry[i]['entry_category']['name']).replace(/\"/g, "")}</td>
                `
			
            table.insertAdjacentHTML('beforeend', row);
        }
    }

    function populateWallets() {
        $.ajax({
			type: 'GET',
			url: url_wallet,
			headers: {
				'X-Requested-With': 'XMLHttpRequest',
			},
			success: function(response) {

                wallet_pos = document.getElementById('wallet_row');
                detail_pos = document.getElementById('dynamic_content');
                var counter = 0;
                //?
                var data = JSON.stringify(response)
                data = JSON.parse(data)
                
            
                if(Object.keys(data).length > 0){
                    for(var key in data){
                        
                        if(data.hasOwnProperty(key)){
                            
                            parseWalletData(wallet_pos, counter, data[counter].name, data[counter].id)
                            parseDetail(
                                detail_pos,
                                counter, 
                                data[counter].name, 
                                data[counter].id,
                                data[counter].viewable,
                                data[counter].date_added,
                                data[counter].entry,
                                data[counter].expense_sum,
                                data[counter].income_sum,
                            )
                            counter += 1;
                        }
                    }
                }
                var first_loaded_wallet_id = $('.row_wallet_instance:first').attr('data_wallet');
                var wallet_id_form = $('#id_wallet_entry_id')
                
                wallet_id_form.val(first_loaded_wallet_id);
        
                $('.row_wallet_instance').bind('click', function() {
                    $('.info_instance_div').fadeOut('fast');
                    var divId= $(this).attr('data_wallet');
                    wallet_id_form.val(divId);
                    setTimeout(function(){
                        $('#'+ divId).fadeIn('fast')
                    }, 300);
                });
             
			},
			error: function(response) {
				
			}
	});}
    
	$("#budget_form").submit(function(e) {
		e.preventDefault();
		var serializedData = $(this).serialize();
		$.ajax({
			type: 'POST',
			url: url_entry,
			headers: {
				"X-Requested-With": "XMLHttpRequest",
			},
			data: serializedData,
			success: function(response) {

                runWhistles()
                
                
			
			},
			error: function(response) {
		
			}
		})
	})

    $("#wallet_form").submit(function(e) {
		e.preventDefault();
		var serializedData = $(this).serialize();
        console.log(serializedData)
		$.ajax({
			type: 'POST',
			url: url_wallet,
			headers: {
				"X-Requested-With": "XMLHttpRequest",
			},
			data: serializedData,
			success: function(response) {
                runWhistles();
			},
			error: function(response) {
		
			}
		})
	})

    

    populateWallets()



}