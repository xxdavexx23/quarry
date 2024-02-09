/**
 * API To Fetch Data
 * Returns data as JSON {ID: 1, Hero: "Batma"}
 */
export const fetchData = async () => {
    const response = await fetch("http://192.168.1.6:5000/data");
    return response.json();
};