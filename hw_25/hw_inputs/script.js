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
      {'key': "name", value: "post"},
      {'key': "placeholder", value: "Enter post"},
      {'key': "minlength", value: 3},
      {'key': "maxlength", value: 255},
      {'key': "required", value: true},
    ],
  ],
}

class myDiv {
  constructor(settings) {
    this.btn = document.createElement("button")
    this.createHtml(settings.action, settings.method)
    settings.inputs.forEach(inputParams => this.addInput(inputParams))
    this.addBtn()
  }

  createHtml() {
    this.htmlDiv = document.createElement("div")
    this.htmlDiv.style.justifyItems= 'center'
    this.htmlDiv.style.display = 'grid'
    this.htmlDiv.style.paddingTop = '20px'

    let header = document.createElement('h1')
    header.style.color = 'white'
    header.innerText = 'Post form'
    header.style.marginBottom = '16px'
    this.htmlDiv.appendChild(header)
    let d = document.createElement("div")
    d.className = "input-group mb-3 grid text-center"
    d.style.justifyContent = 'center'
    d.appendChild(this.htmlDiv)
    document.body.style.backgroundColor = '#035565'
    document.body.appendChild(d)
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
    this.btn.addEventListener("click", () => {
      if (input.required && input.value === '') {
          alert(`input name: ${input.name} can't be empty`)
      }
    })
    this.htmlDiv.appendChild(input)
    this.htmlDiv.appendChild(p)
  }

  addBtn() {
    this.btn.type = "submit"
    this.btn.id = "submit"
    this.btn.className = "btn btn-secondary btn-sm"
    this.btn.innerText = "Submit"
    let div = document.createElement("div")
    div.appendChild(this.btn)
    this.htmlDiv.appendChild(div)
    div.className = "d-flex flex-row-reverse"
  }
}

let div = new myDiv(settings)
