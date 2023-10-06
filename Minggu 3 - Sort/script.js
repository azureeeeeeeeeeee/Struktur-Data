const list_element = document.getElementById('list-element');
const sort_steps_element = document.querySelector('.sort-steps');
const list_input = document.getElementById('list-input');
const push_button = document.getElementById('push-button');
const clear_button = document.getElementById('clear-button');
const sort_button = document.getElementById('sort-button'); // Add this line
let numbers = [];

function PushNumber() {
  numbers.push(Number(list_input.value));
  updateListDisplay(); // Update the displayed list
  console.log(numbers);
}

function updateListDisplay() {
  list_element.innerHTML = `[ ${numbers.join(', ')} ]`;
}

function ClearList() {
  list_element.innerHTML = '';
  numbers = [];
  sort_steps_element.innerHTML = '';
}

function BubbleSort(arr) {
  let steps = [];
  const n = arr.length;
  for (let i = 0; i < n - 1; i++) {
    for (let j = 0; j < n - i - 1; j++) {
      if (arr[j] > arr[j + 1]) {
        // Swap arr[j] and arr[j+1]
        let temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;

        steps.push([...arr]); // Store the current state of the array
      }
    }
  }
  return steps;
}

sort_button.addEventListener('click', () => {
  const steps = BubbleSort(numbers);
  visualizeSortSteps(steps);
});

function visualizeSortSteps(steps) {
  sort_steps_element.innerHTML = ''; // Clear previous visualization
  for (let i = 0; i < steps.length; i++) {
    const stepElement = document.createElement('div');
    stepElement.textContent = steps[i].join(', ');
    sort_steps_element.appendChild(stepElement);
  }
}

push_button.addEventListener('click', PushNumber);
clear_button.addEventListener('click', ClearList);
