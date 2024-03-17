document.getElementById('urlForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    const websiteUrl = document.getElementById('websiteUrl').value;

    try {
        const response = await fetch('/api/extract-links', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ url: websiteUrl })
        });

        if (!response.ok) {
            throw new Error('Failed to extract links');
        }

        const links = await response.json();
        displayLinks(links);
    } catch (error) {
        console.error('Error:', error);
    }
});

function displayLinks(links) {
    const linksContainer = document.getElementById('linksContainer');
    linksContainer.innerHTML = '<h2>Extracted Links:</h2>';
    const ul = document.createElement('ul');

    links.forEach(link => {
        const li = document.createElement('li');
        li.textContent = link;
        ul.appendChild(li);
    });

    linksContainer.appendChild(ul);
}
