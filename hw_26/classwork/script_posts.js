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

    this.postsDiv = document.createElement('div') // div for displaying postss
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
          body[input.name] = input.value
          if (!input.readOnly) {
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
            let post = new Post(postData)
            this.postsDiv.appendChild(post.htmlPost)
            this.posts.push(post)
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
    this.htmlPost.style.textAlign = 'center'
  }

  renderPost() {
    let div = document.createElement('div')
    div.style.backgroundColor = 'rgba(0, 0, 0, 0.12)'
    div.style.borderRadius = '36px'
    div.style.textAlign = 'center'
    let postHeader = document.createElement('h1')
    postHeader.innerText = 'POST'
    postHeader.style.marginBottom = '0'
    postHeader.style.marginTop = '36px'
    let commentsHeader = document.createElement('h2')
    commentsHeader.innerText = 'COMMENTS'
    commentsHeader.style.marginBottom = '0'
    commentsHeader.style.marginTop = '36px'
    let title = document.createElement('p')
    title.innerText = this.title
    let body = document.createElement('p')
    body.innerText = this.body
    let activeDiv = document.createElement('div')
    let changeBtn = document.createElement('button')
    changeBtn.innerText = 'Change'
    changeBtn.className = 'btn btn-info'
    changeBtn.style.padding = '2px 4px 2px 4px'
    changeBtn.style.marginRight = '2px'
    let deleteBtn = document.createElement('button')
    deleteBtn.innerText = 'Delete'
    deleteBtn.className = 'btn btn-warning'
    deleteBtn.style.padding = '2px 6px 2px 6px'
    activeDiv.appendChild(changeBtn)
    activeDiv.appendChild(deleteBtn)
    div.appendChild(postHeader)
    div.appendChild(title)
    div.appendChild(body)
    div.appendChild(activeDiv)
    div.appendChild(commentsHeader)

    let commentTextDiv = document.createElement('div')
    fetch(`https://jsonplaceholder.typicode.com/posts/${this.id}/comments`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json'
      }
    })
      .then(response => response.json())
      .then(comments => {
        comments.forEach((comment, index) => {
          let newComment = new Comment(comment, index + 1)

          commentTextDiv.appendChild(newComment.htmlComment)
        })
      })
    div.appendChild(commentTextDiv)

    const data = [this.userId, this.id, this.title, this.body]

    changeBtn.addEventListener('click', () => {
      let inputsDiv = document.createElement('div')
      let inputTitle = document.createElement('input')
      inputTitle.value = data[2]
      inputTitle.className = 'form-control'
      inputTitle.style.marginTop = '6px'
      let inputBody = document.createElement('input')
      inputBody.value = data[3]
      inputBody.className = 'form-control'
      inputBody.style.marginTop = '6px'
      activeDiv.innerText = ''
      inputsDiv.appendChild(inputTitle)
      inputsDiv.appendChild(inputBody)
      let saveBtn = document.createElement('button')
      saveBtn.innerText = 'Save'
      saveBtn.innerText = 'save'
      saveBtn.className = 'btn btn-success'
      saveBtn.style.padding = '2px 6px 2px 6px'
      saveBtn.style.marginTop = '6px'
      activeDiv.style.alignItems = 'center'
      activeDiv.appendChild(inputsDiv)
      activeDiv.appendChild(saveBtn)
      activeDiv.style.alignItems = 'center'

      saveBtn.addEventListener('click', () => {
        data[2] = inputTitle.value
        data[3] = inputBody.value
        console.log({title: data[2], body: data[3]})
        fetch('https://jsonplaceholder.typicode.com/posts', {
          method: 'PATCH',
          body: JSON.stringify({title: data[2], body: data[3]}),
          headers: {
            'Content-Type': 'application/json'
          }
        })
          .then(response => response.json())
          .then(newData => {
            title.innerText = newData.title || data[2]
            body.innerText = newData.body || data[3]

            activeDiv.innerText = ''
            activeDiv.appendChild(changeBtn)
            activeDiv.appendChild(deleteBtn)
          })
        .catch(err => {
          console.log("there is an error")
        });
      })
    })

    deleteBtn.addEventListener('click', () => {
      fetch('https://jsonplaceholder.typicode.com/posts', {
        method: 'DELETE',
      })
        .then(() => div.innerText = '')
    })
    return div
  }
}


class Comment {
  constructor({postId, id, name, email, body}, numberOfComment) {
    this.postId = postId
    this.id = id
    this.name = name
    this.email = email
    this.body = body
    this.numberOfComment = numberOfComment
    this.htmlComment = this.renderComments() // here is div for current comment
  }

  renderComments() {
    let div = document.createElement('div')
    div.style.marginBottom = '10px'
    let commentHeader = document.createElement('p')
    commentHeader.style.fontWeight = '700'
    commentHeader.innerText = `${this.numberOfComment}`
    let name = document.createElement('p')
    name.innerText = this.name
    let email = document.createElement('p')
    email.innerText = this.email
    email.style.fontWeight = '500'
    let body = document.createElement('p')
    body.innerText = this.body

    div.appendChild(commentHeader)
    div.appendChild(name)
    div.appendChild(body)
    div.appendChild(email)
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
    header.style.color = 'Black'
    header.style.marginBottom = '16px'
    this.htmlDiv.appendChild(header)
    // document.body.style.backgroundColor = '#035565'
  }

  addInput(params) {
    let input = document.createElement("input")
    params.map(item => {
      input.setAttribute(item.key, item.value)
    })
    input.style.borderWidth = '1px'
    input.style.borderColor = 'black'
    let p = document.createElement('p')
    p.style.marginLeft = '6px'
    p.style.marginTop = '6px'
    p.style.color = 'red'
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
    this.htmlDiv.appendChild(input)
    this.inputs.push(input)
    this.htmlDiv.appendChild(p)
  }

  addBtn() {
    this.btn.type = "submit"
    this.btn.id = "submit"
    this.btn.className = "btn btn-success btn-sm"
    this.btn.innerText = "Submit"
    let div = document.createElement("div")
    div.appendChild(this.btn)
    div.className = "d-flex flex-row-reverse"
    this.htmlDiv.appendChild(div)
  }
}
let newPostPage = new PostPage()