import Button from './Button'
import React, { useState } from 'react';

const TextView = ({title}) => {
    const [input, setInput] = useState('Thou mother is');
    const [output, setOutput] = useState('')

    const apiRequest = (e) => {
        const endpoint = '/predict'
        const options = {
            method: "POST",
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json',
            },
            credentials: "include",
            body: JSON.stringify({'text':input}),
          };

        fetch(endpoint, options)
        .then((response) => response.json())
        .then((data) =>setOutput(data.output));

    }
    const onClick = (e) => {
        //console.log(input);

        //api request code here - gotta do error handling too!
        apiRequest();
        //setOutput(input);
    }
    return (
        <div>
            <form>
                <label>
                    <input type="text" name="input" 
                    onChange={e => setInput(e.target.value)} 
                    placeholder="Thou mother is"/>
                </label>
            </form>
            <p>{output}</p>
            <div><Button color='blue' text = 'complete' onClick = {onClick}/></div>
        </div>
        
    
    )
}

export default TextView