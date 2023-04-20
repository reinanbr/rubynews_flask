console.log('adding news...')

$('#sendNewsBt').click(()=>{
    console.log('fui clicado')

    var date = new Date()
    $('#timeJs_').val(date.valueOf())
    $('#sendNewsForm').submit()

})