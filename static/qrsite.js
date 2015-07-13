function funcencode(whichradio){
    var qrtext = document.getElementById('qrtext');
    qrtext.style.visibility='visible';
    
    var uploadFile = document.getElementById('uploadFile');
    uploadFile.style.visibility='hidden';

    var decode = document.getElementById('decode');
    decode.checked=false;
}

function funcdecode(whichradio){
    var uploadFile = document.getElementById('uploadFile');
    uploadFile.style.visibility='visible';

    var qrtext = document.getElementById('qrtext');
    qrtext.style.visibility='hidden';

    var encode = document.getElementById('encode');
    encode.checked=false;
}

function show(){
    var decode = document.getElementById('decode');
    var encode = document.getElementById('encode');

    var uploadFile = document.getElementById('uploadFile');
    var qrtext = document.getElementById('qrtext');

    uploadFile.style.visibility=encode.checked?'hidden':'visible';
    qrtext.style.visibility=decode.checked?'hidden':'visible';
}
