class PostPage {
  constructor() {
    this.createHTML()
  }

  createHTML() {
    this.div = document.createElement('div')
    this.div.className = 'accordion'
    this.div.id = 'accordionExample'

    fetch('https://jsonplaceholder.typicode.com/posts', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json'
      }
    })
      .then(response => response.json())
      .then(posts => {
        posts.forEach(item => this.createItem(item))
      })
      .then(() => {
        document.body.appendChild(this.div)
      })
  }

  createItem(item) {
    let postDiv = document.createElement('div')
    postDiv.className = 'accordion-item'

    let hTitle = document.createElement('h2')
    hTitle.className = 'accordion-header'

    let titleBtn = document.createElement('button')
    titleBtn.className = 'accordion-button'
    titleBtn.type = 'button'
    titleBtn.setAttribute('data-bs-toggle', 'collapse')
    titleBtn.setAttribute('data-bs-target', `#collapse${item.id}`)
    titleBtn.setAttribute('aria-expanded', 'false')
    titleBtn.setAttribute('aria-controls', `collapse${item.id}`)
    titleBtn.innerText = item.title

    hTitle.appendChild(titleBtn)

    let outDivBody = document.createElement('div')
    outDivBody.id = `collapse${item.id}`
    outDivBody.className = 'accordion-collapse collapse'
    outDivBody.setAttribute('data-bs-parent', '#accordionExample')

    let inDivBody = document.createElement('div')
    inDivBody.className = 'accordion-body'
    inDivBody.innerText = item.body

    outDivBody.appendChild(inDivBody)
    postDiv.appendChild(hTitle)
    postDiv.appendChild(outDivBody)
    this.div.appendChild(postDiv)
  }
}

let post = new PostPage()
