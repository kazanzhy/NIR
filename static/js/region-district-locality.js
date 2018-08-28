$(document).ready(function(){
    $('#id_region').change(function(){
        regionId = $(this).val();
        $.ajax({
            url: '/api/districts/',
            data: {'region': regionId},
            success: function(data){
                $('#id_district').empty().append($('<option></option>').val('').html('---------'));
                $('#id_locality').empty().append($('<option></option>').val('').html('---------'));
                $.each(data, function(id, district){
                    $('#id_district').append($('<option></option>').val(id).html(district));
                });
            }
        });
        return false;
    })
    $('#id_district').change(function(){
        districtId = $(this).val();
        request_url = '/api/localities/';
        $.ajax({
            url: request_url,
            data: {'district': districtId},
            success: function(data){
                $('#id_locality').empty().append($('<option></option>').val('').html('---------'));
                $.each(data, function(id, locality){
                    $('#id_locality').append($('<option></option>').val(id).html(locality));
                });
            }
        });
        return false;
    })

});
