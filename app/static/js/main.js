
const messageFromCategory = category =>{
    const lista = {
        'success':'Proceso exitoso!',
        'info' : 'Atención!',
        'error' : 'Oooops...!'
    }
    return lista[category]
}




function showMessageAlert(category, message) {
    Swal.fire({
        icon: category,
        title: messageFromCategory(),
        text: message,
      })
}