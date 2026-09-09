package com.dlp;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class Main {

    private static final String LOG_FILE = "dlp_audit_events.log";

    public static void main(String[] args) {
        System.out.println("=================================================================");
        System.out.println("  DATA LOSS PREVENTION (DLP) PROTOTYPE V1 - ISO 27001 / NIST");
        System.out.println("=================================================================\n");

        DLPEngine engine = new DLPEngine();

        if (args.length > 0) {
            File targetFile = new File(args[0]);
            processFile(engine, targetFile);
        } else {
            System.out.println("[*] No target file passed. Running automated test scan on 'test_files/'...\n");
            File testDir = new File("test_files");
            if (testDir.exists() && testDir.isDirectory()) {
                File[] files = testDir.listFiles();
                if (files != null && files.length > 0) {
                    for (File file : files) {
                        if (file.isFile()) {
                            processFile(engine, file);
                        }
                    }
                }
            } else {
                System.out.println("[-] Directory 'test_files/' not found.");
            }
        }
    }

    private static void processFile(DLPEngine engine, File file) {
        try {
            System.out.println("[>] Intercepting File Operation: " + file.getName());
            DLPEngine.ScanResult result = engine.scanFile(file);

            if (result.isSensitive()) {
                System.out.println("    [!] POLICY VIOLATION DETECTED!");
                System.out.println("    [!] Rules Triggered : " + result.getDetectedRules());
                System.out.println("    [!] Action Enforcement: BLOCK EGRESS & QUARANTINE");
                System.out.println("    [!] Inspection Latency: " + result.getScanTimeMs() + " ms");
                logSecurityEvent(file.getName(), "BLOCKED", result.getDetectedRules().toString(), result.getScanTimeMs());
            } else {
                System.out.println("    [+] Status           : COMPLIANT (No Sensitive Tokens Found)");
                System.out.println("    [+] Action Enforcement: ALLOW OPERATION");
                System.out.println("    [+] Inspection Latency: " + result.getScanTimeMs() + " ms");
                logSecurityEvent(file.getName(), "ALLOWED", "NONE", result.getScanTimeMs());
            }
            System.out.println("-----------------------------------------------------------------");
        } catch (IOException e) {
            System.err.println("[-] Error reading file: " + file.getAbsolutePath() + " - " + e.getMessage());
        }
    }

    private static void logSecurityEvent(String filename, String action, String ruleTriggered, long latencyMs) {
        String timestamp = LocalDateTime.now().format(DateTimeFormatter.ISO_LOCAL_DATE_TIME);
        String logEntry = String.format("[%s] [DLP_AGENT] FILE: %s | ACTION: %s | VIOLATIONS: %s | LATENCY: %d ms%n",
                timestamp, filename, action, ruleTriggered, latencyMs);

        try (FileWriter writer = new FileWriter(LOG_FILE, true)) {
            writer.write(logEntry);
        } catch (IOException e) {
            System.err.println("[-] Failed to write to audit log: " + e.getMessage());
        }
    }
}
