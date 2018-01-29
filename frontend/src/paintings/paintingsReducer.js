import { FETCH_PAINTINGS_FULFILLED } from './paintingsActions';

const defaultState = {}

const paintings = (state=defaultState, action) => {
  switch (action.type) {
    case FETCH_PAINTINGS_FULFILLED: {
      return Object.assign({}, state, {
        paintings: action.payload
      });
    }
    default:
      return state;
  }
}

export default paintings;