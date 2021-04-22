function check() {
    if (document.getElementById('search').value == ""){
        alert("検索ワードを入力して下さい")
        return false;
    } 
}

eel.expose(js_function);
function js_function(args) {
    return document.getElementById(args).value
}

async function run () {
    if (document.getElementById('search').value == ""){
        alert("検索ワードを入力して下さい")
        return false
    } else {
        /*console.log(document.getElementById('search').value)*/
        let res = await eel.kimetsu_search(document.getElementById('search').value)();
        console.log(res);
        document.getElementById('result').innerHTML=res
    }
    
}


/*
<script type="text/javascript">
async function run () {
    let val = await eel.kimetsu_search(document.getElementById('search').innerHTML)();
    document.getElementById('result').innerHTML=val
}
run();
</script>
*/