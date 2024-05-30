let forms = document.querySelectorAll('.form_place')
    radio = document.querySelectorAll('.radio_place')
    form_radio = document.querySelector('.form_radio')
    form_tref = document.querySelector('#form_trefolya')

console.log(radio)



function clear_forms() {
    console.log()
    forms.forEach(element => {
        element.style='display:none;'
    });
}

function read_file(file) {
    let reader = new FileReader();
    reader.onload = () => {
        console.log(reader.result);
    }
    reader.readAsText(file)

}

for (let i = 0; i < radio.length; i++) {
    radio[i].addEventListener('change', ()=>{
        clear_forms()
        forms[i].style = 'display: block;'
        form_radio.style='display:none;'
    })
}


clear_forms();

// forms.forEach(form => {
//     form.addEventListener('submit', ()=>{
//         form.preventDefault();
//         let name = form.querySelector('[name="name"]').value;
//         console.log(name)
//     })
// });

// form_tref.addEventListener('submit', ()=>{
//     form.preventDefault();
//     let name = form.querySelector('[name="name"]').value;
//     console.log(name)
// })

form_tref.addEventListener("submit", getFormValue);
function getFormValue(event) {
    const name = form_tref.querySelector('[name="name"]')
    files = form_tref.querySelector('[name="file"]').files;
    console.log(name.value)
    for (file of files){
        read_file(file)
    }
}
