$(document).ready(function() {
    $('.to-favorite').on('click', function(e) {
        e.preventDefault();
        let pk_photo = e.target.id;
        url = `http://127.0.0.1:8000/api/photo/${ pk_photo }/to_favorite/`

    fetch(url)
    .then((response) => {
        document.getElementById(pk_photo).innerText = 'Удалить из избранного'
        $(this).removeClass('to-favorite').addClass('from-favorite');
        return response;
        })
    });

    $('.from-fav').on('click', function(e) {
        e.preventDefault();
        let pk_photo = e.target.id;
        url = `http://127.0.0.1:8000/api/photo/${ pk_photo }/from_favorite/`

    fetch(url)
    .then((response) => {
        document.getElementById(pk_photo).innerText = 'Добавить в избранное'
        $(this).removeClass('from-favorite').addClass('to-favorite')
        return response;
        })
    })
    })
