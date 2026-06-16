export default async function handler(request, response) {
    const queryString = new URL(request.url, `http://${request.headers.host}`).search;

    const targetUrl = `https://api.open-meteo.com/v1/forecast${queryString}`;

    try {
        const openMeteoResponse = await fetch(targetUrl);

        if (!openMeteoResponse.ok) {
            return response.status(openMeteoResponse.status).json({
                error: `Open-Meteo returned status ${openMeteoResponse.status}`
            });
        }

        const data = await openMeteoResponse.json();

        return response.status(200).json(data);

    } catch (error) {
        return response.status(500).json({
            error: 'Vercel proxy failed to fetch weather data',
            details: error.message
        });
    }
}