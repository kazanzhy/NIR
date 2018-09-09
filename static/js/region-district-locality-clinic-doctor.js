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
    $('#id_locality').change(function(){
        localityId = $(this).val();
        request_url = '/api/clinics/';
        $.ajax({
            url: request_url,
            data: {'locality': localityId},
            success: function(data){
                $('#id_clinic').empty().append($('<option></option>').val('').html('---------'));
                $.each(data, function(id, clinic){
                    $('#id_clinic').append($('<option></option>').val(id).html(clinic));
                });
            }
        });
        return false;
    })
    $('#id_clinic').change(function(){
        clinicId = $(this).val();
        request_url = '/api/doctors/';
        $.ajax({
            url: request_url,
            data: {'clinic': clinicId},
            success: function(data){
                $('#id_doctor').empty().append($('<option></option>').val('').html('---------'));
                $.each(data, function(id, doctor){
                    $('#id_doctor').append($('<option></option>').val(id).html(doctor));
                });
            }
        });
        return false;
    })

});
