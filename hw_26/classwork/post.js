class PostPage {
  constructor() {
    this.renderPage()
    this.posts = []
  }

  renderPage() {
    let htmlPostsBlock = this.renderPostsBlock()
    fetch('https://jsonplaceholder.typicode.com/posts')
      .then(response => response.json())
      .then(function (json) {
        json.forEach(function (postData) {
          let post = new Post(postData)
          htmlPostsBlock.innerHTML += post.htmlPost
          this.posts.push(post)
        })
      })
  }

  renderPostsBlock() {
    this.htmlPostsBlock = document.createElement("div")
    this.htmlPostsBlock.className = "accordion"
    this.htmlPostsBlock.id = "accordionExample"
    document.body.appendChild(this.htmlPostsBlock)
    return this.htmlPostsBlock
  }
}