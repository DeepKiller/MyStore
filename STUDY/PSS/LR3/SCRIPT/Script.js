var elem = document.getElementById("SideBarButton");
elem.onclick = function(){
    var bar = document.getElementById("SideBar");
    if(bar.className == "SideBarOpen"){
        bar.className = "SideBarClose";
        elem.className ="SideBarClose";
        document.getElementById("1a").className = "Hide";
        document.getElementById("2a").className = "Hide";
        document.getElementById("3a").className = "Hide";
    }
    else{
        bar.className = "SideBarOpen";
        elem.className ="SideBarOpen";
        document.getElementById("1a").className = "Visible";
        document.getElementById("2a").className = "Visible";
        document.getElementById("3a").className = "Visible";
    }
}
