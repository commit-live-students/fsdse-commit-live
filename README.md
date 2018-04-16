<h2>Form</h2>
Props: 
    onValidSubmit : function | required

<h2>FormElement</h2>

Props : 
1. valueLink : function(stateComponent, path, onUpdate[optional])
2. label : “First Name”
3. required : false | optional | default - false
4. helpText: string | optional 
5. hint : {
      title : React Element,
      description : React Element
    } | optional
  6. validations : [{
      type: enum constant[error | warning] | default: error
      validation: function(value: anything) => returns a boolean,
      message: string | required
    }]
  7. control : {
      className : ‘’ | optional
		  type: ElementType,
      settings : {
        // all settings will act the props to material-ui/core element
		  }
	} constant | required
  
  
<h3>ElementTypes </h3> 

```Text```
  maxLength : number
  placeholder: string
  endAdornment: ReactElement
  startAdornment: ReactElement
  type: text|password
  
```TexArea```
  maxLength : number
  rows: number
  placeholder: string

`RadioGroup`
options: [{
key: string
label: (ReactElement)/String,
}],
columns: number

`CheckboxGroup` => (value will always be an array)
options: [{
key: string
label: (ReactElement)/String,
}],
columns: number

`Select` => (if multiple value will always be an array)
options: [{
key: string
label: (ReactElement),
labelString: string | optional (Required if label is not string)
}],
multiple : boolean

`SearchableSelect` => (if multiple value will always be an array)
options: [{
key: string
label: (ReactElement),
labelString: string | optional (Required if label is not string)
}],
multi: boolean,

`Switch` => (always returns boolean value)
onLabel : ReactElement
offLabel : ReactElement

`DateTimePicker`
format : string
minDate : timestamp,
maxDate : timestamp

`DatePicker`
format : string
minDate : timestamp,
maxDate : timestamp

`FileUpload`
maxFiles : number | optional | defaults to 1
fileFormats : string | required

`AutoComplete` => (if multiple value will always be an array)
source : function (query){
returns searchResult: {
total: number,
entities: [{}],
objects:{}
}
},
renderer : function(entity, objects){
returns React Element/String
}
labelRenderrer: function(entity, objects){
returns React Element/String
}
multiple : boolean
