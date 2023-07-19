const settings = {
  inputs: [
    [
      {'key': "class", value: "form-control input-number"},
      {'key': "type", value: "userId"},
      {'key': "id", value: "1"},
      {'key': "name", value: "userId"},
      {'key': "value", value: "1"},
      {'key': "readonly", value: true},
    ],
    [
      {'key': "class", value: "form-control input-text"},
      {'key': "type", value: "text"},
      {'key': "id", value: "2"},
      {'key': "name", value: "title"},
      {'key': "placeholder", value: "Enter title"},
      {'key': "minlength", value: 3},
      {'key': "maxlength", value: 255},
      {'key': "required", value: true},
    ],
    [
      {'key': "class", value: "form-control input-text"},
      {'key': "type", value: "text"},
      {'key': "id", value: "3"},
      {'key': "name", value: "body"},
      {'key': "placeholder", value: "Enter post"},
      {'key': "minlength", value: 3},
      {'key': "maxlength", value: 255},
      {'key': "required", value: true},
    ],
  ],
}


class PostPage {
  constructor() {
    let inputsDiv = document.createElement('div')
    inputsDiv.className = "input-group mb-3 grid text-center"
    inputsDiv.style.justifyContent = 'center'
    this.inputsForm = new myDiv(settings)
    inputsDiv.appendChild(this.inputsForm.htmlDiv)

    this.postsDiv = document.createElement('div') // div for displaying posts
    this.createHTML()
    document.body.appendChild(inputsDiv)
    document.body.appendChild(this.postsDiv)
    this.posts = []
  }

  createHTML() {
    fetch('https://jsonplaceholder.typicode.com/posts', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json'
      }
    })
      .then(response => response.json())
      .then(posts => {
        posts.forEach(post => {
          let newPost = new Post(post)
          this.posts.push(newPost)
          newPost.htmlPost.style.marginTop = '0'
          this.postsDiv.appendChild(newPost.htmlPost)
        })
      })

    this.inputsForm.btn.addEventListener("click", () => {
      let inputTitle = this.inputsForm.inputs[1]
      let inputBody = this.inputsForm.inputs[2]
      if (inputTitle.value !== '' && inputBody.value !== '') {
        let body = {'id': this.posts.length + 1}
        this.inputsForm.inputs.forEach(input => {
          console.log(input.name)
          body[input.name] = input.value
          if (!input.readOnly) {
            console.log(body)
            input.value = ""
          }
        })
        fetch('https://jsonplaceholder.typicode.com/posts', {
          method: 'POST',
          body: JSON.stringify(body),
          headers: {
            'Content-Type': 'application/json'
          }
        })
          .then(response => response.json())
          .then(postData => {
            console.log(postData)
            let post = new Post(postData)
            this.postsDiv.appendChild(post.htmlPost)
            this.posts.push(post)
            console.log(this.posts)
          })
      }
    })
  }
}

class Post {
  constructor({userId, id, title, body}) {
    this.userId = userId
    this.id = id
    this.title = title
    this.body = body
    this.htmlPost = this.renderPost() // here is div for current post
  }

  renderPost() {
    let div = document.createElement('div')
    div.style.backgroundColor = 'black'
    div.style.color = 'white'
    div.style.marginBottom = '10px'
    let postHeader = document.createElement('h1')
    postHeader.innerText = 'POST'
    postHeader.style.color = 'white'
    postHeader.style.backgroundColor = 'black'
    postHeader.style.marginBottom = '0'
    postHeader.style.marginTop = '36px'
    let title = document.createElement('p')
    title.innerText = this.title
    let body = document.createElement('p')
    body.innerText = this.body
    let buttonsDiv = document.createElement('div')
    let changeBtn = document.createElement('button')
    changeBtn.innerText = 'Change'
    let deleteBtn = document.createElement('button')
    deleteBtn.innerText = 'Delete'
    buttonsDiv.appendChild(changeBtn)
    buttonsDiv.appendChild(deleteBtn)
    div.appendChild(postHeader)
    div.appendChild(title)
    div.appendChild(body)
    div.appendChild(buttonsDiv)

    fetch(`https://jsonplaceholder.typicode.com/posts/${this.id}/comments`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json'
      }
    })
      .then(response => response.json())
      .then(comments => {
        comments.forEach(comment => {
          let newComment = new Comment(comment.postId, comment.id, comment.name, comment.email, comment.body)

          let commentHeader = document.createElement('h2')
          commentHeader.innerText = 'COMMENT'

          div.appendChild(commentHeader)
          div.appendChild(newComment.htmlComment)
        })
      })

    const data = [this.userId, this.id, this.title, this.body]
    const deleteButton = document.getElementById('delete')
    deleteBtn.addEventListener('click', () => {
      fetch('https://jsonplaceholder.typicode.com/posts', {
        method: 'DELETE',
        body: JSON.stringify({data}),
        headers: {
          'Content-Type': 'application/json'
        }
      })
        .then(() => div.innerText = '')
    })

    changeBtn.addEventListener('click', () => {
      let inputTitle = document.createElement('input')
      inputTitle.value = data[2]
      inputTitle.style.width = '1000px'
      let inputBody = document.createElement('input')
      inputBody.value = data[3]
      inputBody.style.width = '1000px'
      buttonsDiv.innerText = ''
      buttonsDiv.appendChild(inputTitle)
      buttonsDiv.appendChild(inputBody)
      let saveBtn = document.createElement('button')
      saveBtn.innerText = 'Save'
      saveBtn.style.marginLeft = '20px'
      buttonsDiv.appendChild(saveBtn)
      saveBtn.addEventListener('click', () => {
        data[2] = inputTitle.value
        data[3] = inputBody.value
        fetch('https://jsonplaceholder.typicode.com/posts', {
          method: 'PATCH',
          body: JSON.stringify({data}),
          headers: {
            'Content-Type': 'application/json'
          }
        })
          .then(response => response.json())
          .then(newData => {
            console.log(newData)
            title = newData.title
            body = newData.body
            buttonsDiv.innerText = ''
            let changeBtn = document.createElement('button')
            changeBtn.innerText = 'Change'
            let deleteBtn = document.createElement('button')
            deleteBtn.innerText = 'Delete'
            buttonsDiv.appendChild(changeBtn)
            buttonsDiv.appendChild(deleteBtn)
          })
      })
    })
    return div
  }
}


class Comment {
  constructor(postId, id, name, email, body) {
    this.postId = postId
    this.id = id
    this.name = name
    this.email = email
    this.body = body
    this.htmlComment = this.renderComments() // here is div for current comment
  }

  renderComments() {
    let div = document.createElement('div')
    div.style.backgroundColor = 'black'
    div.style.color = 'white'
    div.style.marginBottom = '10px'
    let name = document.createElement('p')
    name.innerText = this.name
    let email = document.createElement('p')
    email.innerText = this.email
    let body = document.createElement('p')
    body.innerText = this.body

    div.appendChild(name)
    div.appendChild(email)
    div.appendChild(body)
    return div
  }
}

class myDiv {
  constructor(settings) {
    this.inputs = []
    this.htmlDiv = document.createElement("div")
    this.htmlDiv.style.justifyItems= 'center'
    this.htmlDiv.style.display = 'grid'
    this.htmlDiv.style.paddingTop = '20px'
    this.btn = document.createElement("button")
    this.createHtml()
    settings.inputs.forEach(inputParams => this.addInput(inputParams))
    this.addBtn()
  }

  createHtml() {
    let header = document.createElement('h1')
    header.style.color = 'white'
    header.innerText = 'Post form'
    header.style.marginBottom = '16px'
    this.htmlDiv.appendChild(header)
    document.body.style.backgroundColor = '#035565'
  }

  addInput(params) {
    let input = document.createElement("input")
    params.map(item => {
      input.setAttribute(item.key, item.value)
    })
    let p = document.createElement('p')
    p.style.marginLeft = '6px'
    p.style.marginTop = '6px'
    p.style.color = 'yellow'
    input.addEventListener('focus', (event) => {
      if (input.required && input.value === '') {
          p.innerText = `input name: ${input.name} can't be empty`
        } else {
          p.innerText = ''
      }
    })
    input.addEventListener('change', (event) => {
      if (input.required && input.value === '') {
          p.innerText = `input name: ${input.name} can't be empty`
        } else {
          p.innerText = ''
      }
    })
    // this.btn.addEventListener("click", () => {
    //   let body = {}
    //   this.inputs.forEach(input => {
    //     body[input.name] = input.value
    //     if (!input.readOnly) {
    //       console.log(body)
    //       input.value = ""
    //     }
    //   })
    //   fetch('https://jsonplaceholder.typicode.com/posts', {
    //     method: 'POST',
    //     body: JSON.stringify(body),
    //     headers: {
    //         'Content-Type': 'application/json'
    //     }
    //       .then(response => response.json())
    //       .then(function (postData) {
    //         let post = new Post(postData)
    //         htmlPostsBlock.appendChild(post.htmlPost)
    //         postPage.posts.push(post)
    //       })
    //   })
    // })
    this.htmlDiv.appendChild(input)
    this.inputs.push(input)
    this.htmlDiv.appendChild(p)
  }

  addBtn() {
    this.btn.type = "submit"
    this.btn.id = "submit"
    this.btn.className = "btn btn-secondary btn-sm"
    this.btn.innerText = "Submit"
    let div = document.createElement("div")
    div.appendChild(this.btn)
    div.className = "d-flex flex-row-reverse"
    this.htmlDiv.appendChild(div)
  }
}
let newPostPage = new PostPage()