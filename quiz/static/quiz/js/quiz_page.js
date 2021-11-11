const url = window.location.href;
const myBox = document.getElementById('box')
const quizBox = document.getElementById('quiz-box')
const scoreBox = document.getElementById('score-box')
const resultBox = document.getElementById('result-box')
const imgBox = document.getElementById("image-quiz-box")
const quizForm = document.getElementById('quiz-form')
const submit_button = document.getElementById("submit")
const csrf = document.getElementsByName('csrfmiddlewaretoken')

var all_questions ,quiz_id ;


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

        <div class="mb-2" >
            <hr>
            <b> Question ${question_id + 1} :  ${question} </b>
            <hr>
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
    const imgDiv = document.createElement("div")
    const cls = ["container-images-quiz","w3-panel" ,"w3-topbar", "w3-bottombar", "w3-border-red" ,"w3-pale-red"]
    imgDiv.classList.add(...cls)
    images.forEach(image=>{

        imgDiv.innerHTML +=
        `
            <div class="col-sm-4 text-center">
                <img src="/static/learn/img/items/${image[1]}.jpg"  class="img-responsive">
            </div>

        `
    })
    imgDiv.innerHTML +=``
    quizBox.append(imgDiv);


//    quizBox.innerHTML +=
//    `
//    <div >
//        <p style="color:red;">${correct}</p>
//        <p>${description}</p>
//    </div>
//    `
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
            dataType: 'json',
            data:  { 'all_questions' : JSON.stringify(all_questions) , 'csrfmiddlewaretoken' : csrf[0].value  ,'quiz_id':quiz_id} ,
            success: function(response){
                    const results = response.results
                    console.log(results)
                    quizForm.classList.add("hidden")
                    submit_button.classList.add("hidden")

                    scoreBox.innerHTML = `${response.passed ? 'Congratulations! ' : 'Ups..:( '} ${response.user} , Your score is ${response.score}%`//.toFixed(2)

                    results.forEach(res=>{

                        const resDiv = document.createElement("div")
                        const imgDiv = document.createElement("div")

                        for (const [question, resp] of Object.entries(res)){
                            var answer = resp['answered']
                            var correct = resp['correct_answer']
                            var description = resp['description']
                            var images = resp['images']

                            resDiv.innerHTML +=  ` <b>Question ${question}</b> : <br>`
                            const cls = ['container-images', 'text-light', 'h5']
                            resDiv.classList.add(...cls)
                            resDiv.setAttribute("id","res-container")


                            const cls2 = ["container-images-results"]
                            imgDiv.classList.add(...cls2)


                            if (resp['answered']==null) {
                                resDiv.innerHTML += '- not answered'
                                resDiv.innerHTML += ` Correct answer: ${correct} <br>`
                                resDiv.innerHTML += ` <u>Description:</u>  ${description} <br>`
                                resDiv.classList.add('bg-danger')

                                images.forEach(image=>{
                                    imgDiv.innerHTML +=
                                    `
                                        <div class="col-sm-4 text-center">
                                        <a href="/learn/${image[0]}">
                                            <img src="/static/learn/img/items/${image[1]}.jpg" id="${question}" alt="${image}" class="img-responsive">
                                        </a>
                                        </div>

                                    `
                                })

                            }
                            else {


                                if (answer == correct) {
                                    resDiv.classList.add('bg-success')
                                    resDiv.innerHTML += ` Answered: ${answer} <br>`
                                    resDiv.innerHTML += ` <u>Description:</u>  ${description} <br>`
                                    images.forEach(image=>{
                                    imgDiv.innerHTML +=
                                    `
                                        <div class="col-sm-4 text-center">
                                            <a href="/learn/${image[0]}">
                                            <img src="/static/learn/img/items/${image[1]}.jpg" id="${question}" alt="${image}" class="img-responsive">
                                        </a>
                                        </div>

                                    `
                                })

                                } else {
                                    resDiv.classList.add('bg-danger')
                                    resDiv.innerHTML += ` Correct answer: ${correct} <br>`
                                    resDiv.innerHTML += ` Answered: ${answer} <br>`
                                    resDiv.innerHTML += ` <u>Description:</u>  ${description} <br>`
                                    images.forEach(image=>{
                                    imgDiv.innerHTML +=
                                    `
                                        <div class="col-sm-4 text-center">
                                            <a href="/learn/${image[0]}">
                                            <img src="/static/learn/img/items/${image[1]}.jpg" id="${question}" alt="${image}" class="img-responsive">
                                        </a>
                                        </div>

                                    `
                                })
                                }
                            }
                        }
                        imgDiv.innerHTML += ` <hr> `
                        resDiv.append(imgDiv)
                        resultBox.append(resDiv)



                    })
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
        all_questions =data["data"];
        quiz_id=data["quiz_id"]
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
        console.log(all_questions);
        send_to_result_page(all_questions)
        //window.location.href = url+ "results"
        //save final response and redirect to results
        // send Json to python view
        //redirect to final page

    }
    
    //send data
});


