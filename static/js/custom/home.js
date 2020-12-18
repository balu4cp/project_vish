
  (function (window) {






    FFS = {}

    GBL = {}


  var userLoginValidator = $("#createUser").validate({
    ignore: [],
    errorElement: 'small',
    errorClass: 'error text-danger',
    errorPlacement: function (error, element) {
      if (element.parent().hasClass("input-group")) {
        error.appendTo(element.parent().parent());
      } else {
        error.appendTo(element.parent());
      }
    },
    rules: {
      name: {
        required: true,
      },
      pswd: {
        required: true,
      },
    },
    messages: {
      name: {
        required: "Please enter a name"
      },
      pswd: {
        required: "Please enter a user name",
      },

    },
    submitHandler: function() {
      FFS.UserCreate();
    }
  });



    GBL.showLoading = function(){
    $(".loader").removeClass('d-none');
    $(".d-none").removeClass('active');
    }

    GBL.hideLoading = function(){
    $(".loader").addClass('d-none');
    $(".d-none").addClass('active');
    }

    FFS.user_list=ko.observableArray([]);
    FFS.user_id=ko.observableArray('');
    FFS.code=ko.observableArray('');
    FFS.friend=ko.observableArray('');





    FFS.getCookie = function(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
          var cookies = document.cookie.split(';');
          for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
            }
          }
        }
        return cookieValue;
      };
    
  FFS.getRoles = function () {
    var csrftoken = FFS.getCookie('csrftoken');
    $.ajax({
      method: 'GET',
      url: '/api/users',
      data: {},
      dataType: 'json',
      beforeSend: function (xhr, settings) {
        GBL.showLoading();
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
      })
      .done(function (d, textStatus, jqXHR) {
        console.log(d)
        FFS.user_list([])
        FFS.user_list(d)
       })
      .fail(function (jqXHR, textStatus, errorThrown) {
        alert('fail')


      })
      .always(function () {
        GBL.hideLoading();
      })
  }


// FFS.UserCreate=function(){
//   alert(123)
// }


  FFS.UserCreate = function(){
    var csrftoken = FFS.getCookie('csrftoken');
    var formdata = new FormData();
    formdata.append('user_id', FFS.user_id());
    formdata.append('code', FFS.code());
    $.ajax({
      method: 'POST',
      url: '/api/friend/get',
      data: formdata,
      contentType: false,
      processData: false,
      beforeSend: function(xhr, settings) {
        GBL.showLoading();
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
    }).done( function (d, textStatus, jqXHR) {
      FFS.getRoles()
      FFS.friend(d)
      FFS.code('')
      $('#createUser').addClass('d-none');
 setTimeout(function(){ 
  // GBL.hideLoading();
  $(".loader").removeClass('d-none'); }, 1000);     
setTimeout(function(){ 
  // GBL.hideLoading();
  $(".loader").addClass('d-none');
  $('#alert').removeClass('d-none'); }, 5000);
    }).fail( function (jqXHR, textStatus, errorThrown) {
      alert(jQuery.parseJSON( jqXHR.responseText ))

    }).always(function(){
      GBL.hideLoading();
    });
  };
















    })(this);
    function init() {
    if (document.readyState == "interactive") {  
      FFS.getRoles();
      ko.applyBindings(FFS);
      }
    }
    document.onreadystatechange = init;