import OpenAI from 'openai';
import readLineSync from 'readline-sync';

const OPENAI_API_KEY = ''; // Add your OpenAI API Key here

const client= new OpenAI({
    apiKey:OPENAI_API_KEY,
});

function getWeatherDetails (city = '') { 
     if (city.toLowerCase() === 'patiala') return '10°C';
     if (city.toLowerCase() === 'delhi') return '8°C';
     if (city.toLowerCase() === 'jaipur') return '9°C';
     if (city.toLowerCase() === 'udaipur') return '12°C';
     if (city.toLowerCase() === 'guwahati') return '15°C';
}
const tools={
    "getWeatherDetails": getWeatherDetails,
}

const user = 'Hey , what is weather of patiala?';


const SYSTEM_PROMPT =`You are an AI Assistant with START, PLAN, ACTION, Obeservation and Output State. 
Wait for the user prompt and first PLAN using available tools. 
After Planning, Take the action with appropriate tools and wait for Observation based on Action.
Once you get the observations, Return the AI response based on START propmt and observations

Strictly follow the JSON output format as in examples
Available Tools:
-function getWeatherDetails (city: string): string getWeatherDetails is a function that accepts city name as string and retuns the weather details

Example: START { "type": "user", "user": "What is the sum of weather of Patiala and udaipur?" } 
{ "type": "plan", "plan": "I will call the getWeatherDetails for Patiala" } 
{ "type": "action", "function": "getWeatherDetails", "input": "patiala" } 
{ "type": "observation", "observation": "10°C" } 
{ "type": "plan", "plan": "I will call getWeatherDetails for udaipur" } 
{ "type": "action", "plan": "I will call getWeatherDetails for udaipur" }
{ "type": "observation", "observation": "12°C" } 
{ "type": "output", "output": "The sum of weather of Patiala and udaipur is 24°C" }
`;


// client.chat.completions.create({
//     model: 'gpt-4o-mini',
//     messages: [{ role: 'user', content: user}],
// })
// .then((e)=>{
//     console.log(e.choices[0].message.content);
// });
// async function chat() { 
//     const result = await client.chat.completions.create({ 
//         model: 'gpt-4', 
//         messages: [ 
//             {"role": "system", content: SYSTEM_PROMPT},
//             { role: 'user', content: user }], 
//         }); 
//     console.log(result.choices [0].message.content);
// } 
// chat();

const messages = [{ role: 'system', content: SYSTEM_PROMPT }];

while (true) {
    const query = readLineSync.question('>> '); 
    const q = { type: 'user', user: query, };
    messages.push({ role: 'user', content: JSON.stringify(q) }); 
    
    while (true) { 
        const chat = await client.chat.completions.create({ 
            model: 'gpt-4', messages: messages, 
            response_format: { type: 'json_object' }, 
        }); 

        const result = chat.choices[0].message.content;
        messages.push({ role: 'assistant', content:result});
        
        const call = JSON.parse(result);

        if(call.type === 'output') { 
            console.log(call.output);
            break;
        }
        else if(call.type==='action') { 
            const fn = tools[call.function];
            const observation= fn(call.input);
            const obs = { type: 'observation', observation: observation }; 
            messages.push({ role: 'developer', content: JSON.stringify(obs) });
        }

    } 
}
