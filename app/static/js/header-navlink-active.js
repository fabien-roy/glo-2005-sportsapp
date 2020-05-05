let paths = ['sports', 'practice-centers', 'shops', 'equipments', 'users']

window.addEventListener('load', function () {
    for (let path of paths) {
        if (window.location.href.includes('/' + path)) {
            let navlink = document.getElementById('navlink-' + path)
            navlink.classList.add('active')
        }
    }
})
