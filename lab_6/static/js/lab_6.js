$(document).ready(function(){
    $(".chat-text").keypress(function(event) {
        if (event.which === 13) {
            var chat = $("textarea").val();
            $("textarea").val("");
            $(".msg-insert").append('<p class="msg-send">'+chat+'</p>');
            $(".msg-insert").append('<br>');
        }
    });
    $("#shrink-button").click(function() {
        document.getElementById("shrink-button").style.display = "none";
        document.getElementById("expand-button").style.display = "block";
        document.getElementById("chat-body").style.display = "none";
    });
    $("#expand-button").click(function() {
        document.getElementById("shrink-button").style.display = "block";
        document.getElementById("expand-button").style.display = "none";
        document.getElementById("chat-body").style.display = "block";
    });

    // Themes code
    var themes = [
        {"id":0,"text":"Red","bcgColor":"#F44336","fontColor":"#FAFAFA"},
        {"id":1,"text":"Pink","bcgColor":"#E91E63","fontColor":"#FAFAFA"},
        {"id":2,"text":"Purple","bcgColor":"#9C27B0","fontColor":"#FAFAFA"},
        {"id":3,"text":"Indigo","bcgColor":"#3F51B5","fontColor":"#FAFAFA"},
        {"id":4,"text":"Blue","bcgColor":"#2196F3","fontColor":"#212121"},
        {"id":5,"text":"Teal","bcgColor":"#009688","fontColor":"#212121"},
        {"id":6,"text":"Lime","bcgColor":"#CDDC39","fontColor":"#212121"},
        {"id":7,"text":"Yellow","bcgColor":"#FFEB3B","fontColor":"#212121"},
        {"id":8,"text":"Amber","bcgColor":"#FFC107","fontColor":"#212121"},
        {"id":9,"text":"Orange","bcgColor":"#FF5722","fontColor":"#212121"},
        {"id":10,"text":"Brown","bcgColor":"#795548","fontColor":"#FAFAFA"}
    ];
    var selectedTheme = {"Indigo":{"bcgColor":"#3F51B5","fontColor":"#FAFAFA"}};

    // Set default theme in localStorage when first opened
    if (localStorage.getItem("selectedTheme") === null) {
        localStorage.setItem('selectedTheme', JSON.stringify(selectedTheme));
    }

    // Save to local storage
    localStorage.setItem('themes', JSON.stringify(themes));

    var retrievedObject = localStorage.getItem('themes');
    $('.my-select').select2({data: JSON.parse(retrievedObject)});

    var retrievedSelected = JSON.parse(localStorage.getItem('selectedTheme'));
    var key;
    var bcgColor;
    var fontColor;
    for (key in retrievedSelected) {
        if (retrievedSelected.hasOwnProperty(key)) {
            bcgColor=retrievedSelected[key].bcgColor;
            fontColor=retrievedSelected[key].fontColor;
        }
    }

    $("body").css({"background-color": bcgColor});
    if(bcgColor=="#F44336"){
        $("button:not(.apply-button)").css({"background-color": "#2196F3", "color":"#212121"});
    } else {
        $("button:not(.apply-button)").css({"background-color": "#F44336", "color":"#FAFAFA"});
    }

    $('.apply-button').on('click', function(){
        var valueTheme = $('.my-select').val();
        var theme;
        var a;
        var selectedTheme = {};
        for(a in themes){
            if(a==valueTheme){
                var bcgColor = themes[a].bcgColor;
                var fontColor = themes[a].fontColor;
                var text = themes[a].text;
                $("body").css({"background-color": bcgColor});
                if(bcgColor=="#F44336"){
                    $("button:not(.apply-button)").css({"background-color": "#2196F3", "color":"#212121"});
                } else {
                    $("button:not(.apply-button)").css({"background-color": "#F44336", "color":"#FAFAFA"});
                }
                selectedTheme[text] = {"bcgColor":bcgColor,"fontColor":fontColor};
                localStorage.setItem('selectedTheme', JSON.stringify(selectedTheme));
            }
        }
    });
});

// Calculator
var print = document.getElementById('print');
var erase = false;

var go = function(x) {
    if (x === 'ac') {
        print.value = ""
    } else if (x === 'eval') {
        print.value = Math.round(eval(print.value) * 10000) / 10000;
        erase = true;
    } else if (x === 'log' || x === 'sin' || x === 'tan') {
        if (x === 'log') {
            print.value = eval('Math.'+x+'10'+'('+print.value+')').toPrecision(2);
        } else {
            print.value = eval('Math.'+x+'('+toDegrees(print.value)+')').toPrecision(2);
        }
        erase = true;
    } else {
        print.value += x;
    }
};

function toDegrees (angle) {
  return angle * Math.PI/180;
}