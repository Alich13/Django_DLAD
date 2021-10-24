console.log("hello world")
const modalBtns = [...document.getElementsByClassName('modal-button')]
const modalBody = document.getElementById('modal-body-confirm')
const startBtn = document.getElementById('start-button')

const url = "http://127.0.0.1:8000/quiz/"

console.log(window.location.href)
modalBtns.forEach(modalBtn=> modalBtn.addEventListener('click', ()=>{
    const pk = modalBtn.getAttribute('data-pk')
    const numQuestions = modalBtn.getAttribute('data-questions')
    const scoreToPass = modalBtn.getAttribute('data-pass')
    const time = modalBtn.getAttribute('data-time')

    modalBody.innerHTML =
    `
        <div class="h5 mb-3">Are you sure you want to begin ?</div>
        <div  style="font-size:20px;">
            <ul>
                <li>number of questions : <b>${numQuestions}</b></li>
                <li>score to pass : <b>${scoreToPass}</b></li>
                <li>time : <b>${time} </b></li>
            </ul>
        </div>
    `

    startBtn.addEventListener('click', ()=>{
        window.location.href = url + pk

    })
    }))



