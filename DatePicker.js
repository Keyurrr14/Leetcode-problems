import { useEffect, useState } from "react";
import DatePicker from "react-multi-date-picker";

export default function DatePickerComponent(props) {
  const today = new Date();
  const [values, setValues] = useState(props?.multiple ? [today] : today);

  useEffect(() => {
    let dateArray = [];
    if (values) {
      if (props?.multiple) {
        dateArray = values.map((date) => new Date(date));

        // Replace today's date with the first selected date if necessary
        if (
          dateArray.length > 1 &&
          dateArray[0].toDateString() === today.toDateString()
        ) {
          dateArray.splice(0, 1);
        }

        dateArray.sort((a, b) => a - b);
        props.setDatesSelected(dateArray);
      } else {
        props.setDatesSelected(values);
      }
    }
  }, [values]);

  return (
    <DatePicker
      value={values}
      format="DD MMMM YYYY"
      onChange={(dates) => {
        let newValues = Array.isArray(dates) ? dates : [dates];

        if (props?.multiple) {
          newValues = newValues
            .map((date) => new Date(date))
            .filter((date) => date.toDateString() !== today.toDateString());

          // If no dates are selected, fall back to today's date
          if (newValues.length === 0) {
            newValues = [today];
          }
        } else {
          newValues = new Date(dates);
        }

        setValues(newValues);
      }}
    />
  );
}
