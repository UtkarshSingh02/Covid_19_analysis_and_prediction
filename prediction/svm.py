train_ml=data.iloc[:int(datewise.shape[0]*0.95)]
valid_ml=data.iloc[int(datewise.shape[0]*0.95):]
#Only 5% of the data is left for testing

#Intializing SVR Model
svm=SVR(C=1,degree=5,kernel='poly',epsilon=0.01)

#Fitting model on the training data
svm.fit(np.array(train_ml["date"]).reshape(-1,1),np.array(train_ml["casesconfirmed"]).reshape(-1,1))

prediction_valid_svm=svm.predict(np.array(valid_ml["date"]).reshape(-1,1))

model_scores.append(np.sqrt(mean_squared_error(valid_ml["casesconfirmed"],prediction_valid_svm)))
print("Root Mean Square Error for Support Vectore Machine: ",np.sqrt(mean_squared_error(valid_ml["Confirmed"],prediction_valid_svm)))

plt.figure(figsize=(12,6))
prediction_svm=svm.predict(np.array(datewise["date"]).reshape(-1,1))
fig=go.Figure()
fig.add_trace(go.Scatter(x=datewise.index, y=datewise["Confirmed"],
                    mode='lines',name="Train Data for Confirmed Cases"))
fig.add_trace(go.Scatter(x=datewise.index, y=prediction_svm,
                    mode='lines',name="Support Vector Machine Best fit Kernel",
                    line=dict(color='red', dash='dash')))
fig.update_layout(title="Confirmed Cases Support Vectore Machine Regressor Prediction",
                 xaxis_title="Number of days",yaxis_title="Cases",legend=dict(x=0,y=1,traceorder="normal"))
fig.show()
