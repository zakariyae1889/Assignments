let CourseID=document.getElementById("CourseID")
CourseID.onchange=()=>{
 fetch('/CourseID'+CourseID).then(function(response){
    response.json().then(function(data){

        optionHtml="";
        for(CourseID of data.CourseID){
            optionHtml+='<option value="'+CourseID.id+'">'+CourseID.name +'</option>'
        }
        CourseID.innerHTML=optionHtml;

       });
    });
};
  
   