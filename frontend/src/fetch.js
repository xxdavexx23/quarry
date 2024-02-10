/**
 * API To Fetch Data
 * Returns data as JSON {id: number, name: string}
 */
export const fetchData = async () => {
    const response = await fetch("http://18.234.52.80:5000/data");
    return response.json();
};