import {
  convertTimeRange,
  convertTimeRangeStartEnd,
} from "@/services/common.service";
import styles from "@/styles/FormStyles.module.css";
import { useEffect, useState } from "react";
import DatePickerComponent from "./DatePickerComponent";

export default function AddDatesComponent(props) {
  const [dateType, setDateType] = useState(0);
  const [gigDates, setGigDates] = useState();
  const days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"];
  const [finalString, setFinalString] = useState(null);
  const [selectedDays, setSelectedDays] = useState([
    false,
    false,
    false,
    false,
    false,
    false,
    false,
  ]);

  function submitData() {
    props.selectedDates({
      selectedDays: selectedDays,
      gigDates: gigDates,
      dateType: dateType,
      finalString: finalString,
    });
  }

  useEffect(() => {
    setDateType(0);
  }, []);

  function addDay(index) {
    var sDays = [...selectedDays];
    sDays[index] = !sDays[index];
    setSelectedDays(sDays);
  }

  useEffect(() => {
    setFinalString(null);
    calculateDates();
  }, [gigDates, selectedDays, dateType]);

  function calculateDates() {
    if (dateType == 0) {
      var fS = convertTimeRange(gigDates);
      setFinalString(fS);
    } else {
      var fS = convertTimeRangeStartEnd(gigDates, selectedDays);
      if (!fS) {
        return;
      }
      setFinalString(fS);
    }
  }

  return (
    <div className={styles.formContainer + " text-center "}>
      <div className="grid grid-cols-2 gap-x-2">
        <div
          className={
            styles.selectionBox +
            " " +
            (dateType == 0 ? styles.selectionBoxSelected : "")
          }
          onClick={() => {
            setDateType(0);
          }}
        >
          <div>On specific dates</div>
          <div>
            <small>( eg. 01-02-23, 04-06-23 )</small>
          </div>
        </div>
        <div
          className={
            styles.selectionBox +
            " " +
            (dateType == 1 ? styles.selectionBoxSelected : "")
          }
          onClick={() => {
            setDateType(1);
          }}
        >
          <div>For a date range</div>
          <div>
            <small>( eg. 01-02-23 to 04-06-23 )</small>
          </div>
        </div>
      </div>
      {dateType == 0 && (
        <>
          <div className="mt-4">Enter your specific schedule dates</div>
          <div className="mt-4">
            <DatePickerComponent
              multiple={true}
              setDatesSelected={(e) => {
                setGigDates(e);
              }}
            ></DatePickerComponent>
          </div>
          <div className="mt-[300px]">
            {finalString && (
              <>
                Selected dates :<br></br>
                {finalString}
              </>
            )}
          </div>
          <div
            className="primaryButton mt-8"
            onClick={() => {
              submitData();
            }}
          >
            Proceed
          </div>
        </>
      )}
      {dateType == 1 && (
        <>
          <div className="mt-4">
            Select range of dates from the calendar<br></br>
            (Select only the first and the last day of the event)
          </div>
          <div className="mt-4">
            <DatePickerComponent
              multiple={true}
              setDatesSelected={(e) => {
                setGigDates(e);
              }}
            ></DatePickerComponent>
          </div>
          <div className="mt-[300px]">Is it on any specific days?</div>
          <div className="mt-4 flex justify-center">
            {days.map((day, index) => (
              <div
                className={
                  "p-1 inline-block bg-black border text-xs mr-2" +
                  " " +
                  (selectedDays[index] ? styles.selectionBoxSelected : "")
                }
                key={"day_" + index}
                onClick={() => {
                  addDay(index);
                }}
              >
                {day}
              </div>
            ))}
          </div>
          <div className="mt-8">
            {finalString && (
              <>
                Selected dates :<br></br>
                {finalString}
              </>
            )}
          </div>
          <div
            className="primaryButton mt-8"
            onClick={() => {
              submitData();
            }}
          >
            Proceed
          </div>
        </>
      )}
    </div>
  );
}
