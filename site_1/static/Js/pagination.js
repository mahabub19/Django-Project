        
        
//get search form and page link
        let searchForm = document.getElementById('searchForm')
        let pageLink = document.getElementsByClassName('page-link')

        //check if there search form if clieked
        if(searchForm) {
           for(let i=0;i<pageLink.length;i++){
              pageLink[i].addEventListener('click',function (e) {
                e.preventDefault()
                //get  the data attribute 
                let page = this.dataset.page
                // console.log('Clicked page : ' , page )
                // add hidden input to searchform 
                searchForm.innerHTML += `<input value=${page} name="page"  hidden/>`
                //submit searchform 
                searchForm.submit() 
              })
           }
        }