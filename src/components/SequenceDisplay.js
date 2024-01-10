const SequenceDisplay = ({ values }) => (
  <div>
    <ol className="answer">
      {values.map((value) => (
        <li key={value}>{value}</li>
      ))}
    </ol>
  </div>
);

export default SequenceDisplay;
