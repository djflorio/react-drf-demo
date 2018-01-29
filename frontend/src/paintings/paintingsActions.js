export const FETCH_PAINTINGS = 'FETCH_PAINTINGS';
export const FETCH_PAINTINGS_FULFILLED = 'FETCH_PAINTINGS_FULFILLED';
export const FETCH_PAINTINGS_REJECTED = 'FETCH_PAINTINGS_REJECTED';

export const fetchPaintings = () => ({
  type: FETCH_PAINTINGS_FULFILLED,
  payload: [
    {
      name: "Test",
      artist: "Mr. Painter",
      description: "It's a painting",
      retail_price: 1000.00,
      price: 45.50,
      image: "painting.png",
      source: "google.com"
    }
  ]
});