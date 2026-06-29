export default async function handler(request, response) {
    const queryString = new URL(request.url, `http://${request.headers.host}`).search;
    const apiKey = process.env.VITE_WEATHER_API_KEY;

    const targetUrl = `https://customer-api.open-meteo.com/v1/forecast${queryString}&apikey=${apiKey}`;

    try {
        const openMeteoResponse = await fetch(targetUrl);

        if (!openMeteoResponse.ok) {
            const errorText = await openMeteoResponse.text();
            return response.status(openMeteoResponse.status).json({
                error: `Open-Meteo API error`,
                details: errorText
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