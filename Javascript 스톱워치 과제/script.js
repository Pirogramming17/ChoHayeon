let seconds = 0;
let tenMillis = 0;
let intervalId;

const appendTens = document.querySelector('.tenMillis');
const appendSeconds = document.querySelector('.seconds');
const buttonStart = document.querySelector('.btn__start');
const buttonStop = document.querySelector('.btn__stop');
const buttonReset = document.querySelector('.btn__reset');
const ul_recordList = document.querySelector(".recordList");
const li_checkAll = document.querySelector('.checkButton');
const buttonDelete =  document.querySelector('.btn__delete');

// start
buttonStart.onclick = ('click', () => {
    clearInterval(intervalId)
    intervalId = setInterval(operateTimer,10)   
})

//stop
buttonStop.onclick = ("click", () => {
    clearInterval(intervalId)
    let li_recordList = document.createElement("li");
    let btn_check = document.createElement("button");
    btn_check.value = "0";
    let time_recordList = document.createElement("div");
    let btn_delete = document.createElement("button");
    btn_delete.classList.add("hidden");
    time_recordList.innerText = fillTime()
    btn_check.classList.add("checkButton");
    li_recordList.appendChild(btn_check);
    li_recordList.appendChild(time_recordList);
    li_recordList.appendChild(btn_delete);
    ul_recordList.appendChild(li_recordList);
})

//reset
buttonReset.onclick = ("click", () => {
    clearInterval(intervalId)
    tenMillis = 0;
    seconds = 0;
    appendTens.textContent = "00"
    appendSeconds.textContent = "00"
})

//check all li
li_checkAll.onclick = ("click", () => {
    if (li_checkAll.value == "0") {
        li_checkAll.className = "checkButton_yes";
        li_checkAll.value = "1";
        let checkLists = document.querySelectorAll('.checkButton');
        for (let i=0; i<checkLists.length; i++){
            checkLists[i].className  = "checkButton_yes";
            checkLists[i].value = "1";           
        }
    }
    else {
        li_checkAll.className = "checkButton";
        li_checkAll.value = "0";
        let checkLists = document.querySelectorAll('.checkButton_yes');
        for (let i=0; i<checkLists.length; i++){
            checkLists[i].className  = "checkButton";
            checkLists[i].value = "0";
            checkLists[i].onclick = ("click", () => {
                if(checkLists[i].value == "0") {
                    checkLists[i].className  = "checkButton_yes";
                    checkLists[i].value = "1";
                }
                else {
                    checkLists[i].className  = "checkButton";
                    checkLists[i].value = "0";
                }
            })
        }
    }
})

//check one li
document.addEventListener(
    "click",
    function (e) {
        let checkLists = document.querySelectorAll('.checkButton');
        for (let i=1; i<checkLists.length; i++) {
        checkLists[i].onclick = ("click", () => {
            if(checkLists[i].value == "0") {
            checkLists[i].className  = "checkButton_yes";
            checkLists[i].value = "1";
        }
            else {
            checkLists[i].className  = "checkButton";
            checkLists[i].value = "0";
        }
    })
}
    },false);

//delete
buttonDelete.onclick = ("click", () => {
    let deleteLists = document.querySelectorAll('li');
    for (let i=1; i<deleteLists.length; i++) {
        if(deleteLists[i].childNodes[0].value == "1")
            deleteLists[i].remove();
    }
    let checkFirst = document.querySelector('.checkButton_yes');
    checkFirst.className  = "checkButton";
    checkFirst.value = "0";
})

// 10ms 마다 시간에 대한 숫자가 증가
function operateTimer() {
    tenMillis++;
    appendTens.textContent = '0' + tenMillis
    if(tenMillis > 9) {
        appendTens.textContent = tenMillis
        if (tenMillis > 99) {
            seconds++;
            appendSeconds.textContent = '0' + seconds
            tenMillis = 0
            appendTens.textContent = '00'
        }
    }
}

// list 추가
function addList() {
    const newDiv = document.createElement('li')
    li.textContent = '새로운 DOM 객체입니다!'
    recordList.appendChild(newDiv)
}

// 구간 기록 - Time
function fillTime() {
    return String(seconds).padStart(2, "0") + " : " + String(tenMillis).padStart(2, "0")
}