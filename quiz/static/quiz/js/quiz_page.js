var all_questions ;
const url = window.location.href;
const quizBox = document.getElementById('quiz-box')
const scoreBox = document.getElementById('score-box')
const resultBox = document.getElementById('result-box')
const timerBox = document.getElementById('timer-box')



function diplay_quiz(data,i)
{
    const question_id = i;
    console.log(i);
    const data_tuple = data["data"][i];
    const question = data_tuple[0];
    const answers = data_tuple[1];
    console.log(data_tuple);
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
};



$.ajax({
    type: 'GET',
    url: `${url}data`,
    async: false,
    success: function(data)
    {   
        all_questions = data
    },

    error: function(error){

        console.log(error);
    
    }
});




diplay_quiz(all_questions,0);
var k=0 ;
let len = Object.keys(all_questions.data).length;
document.getElementById("submit").addEventListener('click',function()
{
    console.log("cliked");
    // console.log(all_questions)
    
    if (k < len ) {
        k = k +1 ;
        console.log("in before button");
        diplay_quiz(all_questions,k);
      }
    
    //send data
});













