/**
 * API To Fetch Data
 * Returns data as JSON {id: number, name: string}
 */
export const fetchData = async () => {
    const response = await fetch("http://54.234.114.163:5000/data");
    return response.json();
};