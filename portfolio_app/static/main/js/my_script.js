function getToken (name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split (';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim ();
            // Does this cookie string begin with the name we want?
            if (cookie.substring (0 , name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent (cookie.substring (name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getToken ('csrftoken')


const SubmitForm = (event) => {
    event.preventDefault ()
    console.log ('the form was called')
    let post_url = 'http://127.0.0.1:8000/user/contactuser/'
    let request_method = 'Post'
    console.log (post_url)
    console.log (request_method)
    const formData = new FormData ()
    const contact_name = $ ("#id_contact_name").val ()
    const contact_email = $ ("#id_contact_email").val ()
    const contact_subject = $ ("#id_contact_subject").val ()
    const contact_message = $ ("#id_contact_message").val ()
    const to_email = $ ("#id_to_email").val ()
    formData.append ('contact_name' , contact_name)
    formData.append ('contact_email' , contact_email)
    formData.append ('contact_subject' , contact_subject)
    formData.append ('contact_message' , contact_message)
    formData.append ('to_email' , to_email)
    console.log ('these are the data fro mthe form ' ,
        contact_name ,
        contact_email ,
        contact_subject ,
        contact_message ,
        to_email
    )
    console.log (formData)
    $.ajax ({
        url: post_url ,
        type: request_method ,
        headers: {'X-CSRFTOKEN': csrftoken} ,
        data: formData ,
        contentType: false ,
        cache: false ,
        processData: false ,
        success: function (response) {
            alert ('success' , response)
        } ,
        error: function (response) {
            alert (response.responseText)
            console.log (response)
        }
    }).done (function (response) {
        console.log ('response' , response)
    })
}


$ (".submit-form").submit (function (event) {
    event.preventDefault ()
    console.log ('the form was called')
    let post_url = $ (this).attr ("action")
    let request_method = 'Post'
    console.log (post_url)
    console.log (request_method)
    const formData = new FormData ()
    const contact_name = $ ("#id_contact_name").val ()
    const contact_email = $ ("#id_contact_email").val ()
    const contact_subject = $ ("#id_contact_subject").val ()
    const contact_message = $ ("#id_contact_message").val ()
    const to_email = $ ("#id_to_email").val ()
    formData.append ('contact_name' , contact_name)
    formData.append ('contact_email' , contact_email)
    formData.append ('contact_subject' , contact_subject)
    formData.append ('contact_message' , contact_message)
    formData.append ('to_email' , to_email)
    console.log ('these are the data fro mthe form ' ,
        contact_name ,
        contact_email ,
        contact_subject ,
        contact_message ,
        to_email
    )
    console.log (formData)
    $.ajax ({
        url: post_url ,
        type: request_method ,
        headers: {'X-CSRFTOKEN': csrftoken} ,
        data: formData ,
        contentType: false ,
        cache: false ,
        processData: false ,
        success: function (response) {
            alert ('success' , response)
        } ,
        error: function (response) {
            alert (response.responseText)
            console.log (response)
        }
    }).done (function (response) {
        console.log ('response' , response)
    })
})



