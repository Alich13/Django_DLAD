const url = window.location.href;
const quizBox = document.getElementById('quiz-box')
const scoreBox = document.getElementById('score-box')
const resultBox = document.getElementById('result-box')
const timerBox = document.getElementById('timer-box')
const quizForm = document.getElementById('quiz-form')
const csrf = document.getElementsByName('csrfmiddlewaretoken')

var all_questions ;


function diplay_quiz(data,question_id)
{

    const data_tuple = data[question_id];
    const question = data_tuple[0];
    const answers = data_tuple[1];
    const images = data_tuple[2];
    const correct = data_tuple[3];
    const description = data_tuple[4];

    quizBox.innerHTML =
     `
        <hr>
        <div class="mb-2">
            <b>${question_id} / ${question}</b>
        </div>
    `
    answers.forEach(answer=>{
        quizBox.innerHTML += 
        
        `
            <div>
                <input type="radio" class="ans" id="${question_id}" name="${question_id}" value="${answer}">
                <label for="${question_id}">${answer}</label>
            </div>

        `
    })

    images.forEach(image=>{
        quizBox.innerHTML +=

        `
            <div class="col-sm-4 text-center">
                <img src="/static/learn/img/items/${image}.jpg" id="${question_id}" alt="${image}" class="img-responsive">
            </div>

        `
    })
    quizBox.innerHTML +=
    `
    <div >
        <p style="color:red;">${correct}</p>
        <p>${description}</p>
    </div>
    `
};


function save(question_id)
{

    const elements = [...document.getElementsByClassName('ans')]
    const data_ans ={};
    //data_ans['csrfmiddlewaretoken'] = csrf[0].value

    elements.forEach(el=>{
            if (el.checked) {
                data_ans[question_id] = el.value
            } else {
                if (!data_ans[question_id]) {
                    data_ans[question_id] = null
                }
            }

             })

    all_questions[question_id].push(data_ans[question_id])

}

function send_to_result_page() 
{
    $.ajax({
            
            type: 'POST',
            url: `${url}save/`,
            data: all_questions,
            success: function(response){
                const results = response.results
                console.log(results);
                },

            error: function(error){
            console.log(error);
            }

         })
}






$.ajax({
    type: 'GET',
    url: `${url}data`,
    async: false,
    success: function(data)
    {
        all_questions = data;
        all_questions =all_questions["data"];
    },

    error: function(error){
        console.log(error);
    }
});


// after loding the question

diplay_quiz(all_questions,0);
let len = Object.keys(all_questions).length;
console.log(len)
var question_id=0 ;

document.getElementById("submit").addEventListener('click',function()
{
    if (question_id <= (len-2)  ) {
        save(question_id);
        question_id = question_id +1 ;
        diplay_quiz(all_questions,question_id);
        // concatinate user response to data  dict

      }

    else if ( question_id==len-1 ){
        save(question_id);
        all_questions['csrfmiddlewaretoken'] = csrf[0].value
        console.log(all_questions);
        send_to_result_page(all_questions)
        //save final response and redirect to results
        // send Json to python view
        //redirect to final page

    }
    
    //send data
});














