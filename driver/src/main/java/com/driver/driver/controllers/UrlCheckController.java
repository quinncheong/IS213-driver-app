package com.driver.driver.controllers;

import java.io.FileInputStream;
import java.io.IOException;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.FutureTask;

import com.google.auth.oauth2.GoogleCredentials;
import com.google.firebase.FirebaseApp;
import com.google.firebase.FirebaseOptions;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class UrlCheckController {
  DatabaseReference REF;

  public UrlCheckController() throws IOException {
    FileInputStream serviceAccount = new FileInputStream("src/main/resources/assets/privateKey.json");
    FirebaseOptions options = FirebaseOptions.builder()
        .setCredentials(GoogleCredentials.fromStream(serviceAccount))
        // The database URL depends on the location of the database
        .setDatabaseUrl("https://ninja-truck-9fb80-default-rtdb.asia-southeast1.firebasedatabase.app/")
        .build();

    FirebaseApp.initializeApp(options);
    REF = FirebaseDatabase.getInstance().getReference("Drivers");
  }

  public interface FirebaseCallback {
    void onResponse(Object driver);
  }

  public void readData(DatabaseReference ref, FirebaseCallback firebaseCallback) {
    ref.addValueEventListener((ValueEventListener) new ValueEventListener() {
      @Override
      public void onDataChange(DataSnapshot dataSnapshot) {
        Object driver = dataSnapshot.getValue();
        System.out.println(driver);
        firebaseCallback.onResponse(driver);
      }

      @Override
      public void onCancelled(DatabaseError error) {
      }
    });
  }

  @GetMapping("/driver/{driverId}")
  @ResponseBody
  public Map<String, Object> getDriverId(@PathVariable String driverId)
      throws IOException, InterruptedException, ExecutionException {
    DatabaseReference ref = REF.child(driverId);
    Map<String, Object> response = new LinkedHashMap<>();
    response.put("code", 200);
    response.put("data", "none");
    final FutureTask<Object> ft = new FutureTask<Object>(() -> {
    }, new Object());
    readData(ref, new FirebaseCallback() {
      @Override
      public void onResponse(Object driver) {
        response.put("data", driver);
        ft.run();
      }
    });
    ft.get();
    return response;
  }
}
