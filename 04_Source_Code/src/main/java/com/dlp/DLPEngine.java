package com.dlp;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class DLPEngine {

    private static final Map<String, Pattern> SENSITIVE_PATTERNS = new LinkedHashMap<>();

    static {
        // Malaysian NRIC / National ID Pattern
        SENSITIVE_PATTERNS.put("NATIONAL_ID_MY", Pattern.compile("\\b\\d{6}-\\d{2}-\\d{4}\\b|\\b\\d{12}\\b"));
        
        // Credit Card Number (Visa, MasterCard, Amex)
        SENSITIVE_PATTERNS.put("CREDIT_CARD", Pattern.compile("\\b(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|3[47][0-9]{13})\\b"));
        
        // Confidential Markings
        SENSITIVE_PATTERNS.put("CONFIDENTIAL_MARKING", Pattern.compile("(?i)\\b(CONFIDENTIAL|INTERNAL ONLY|STRICTLY PRIVATE|RESTRICTED)\\b"));
        
        // API Keys & Tokens
        SENSITIVE_PATTERNS.put("API_KEY_SECRET", Pattern.compile("(?i)\\b(api[_-]?key|secret[_-]?key|access[_-]?token)\\s*[:=]\\s*['\"]?[A-Za-z0-9_\\-]{16,}['\"]?\\b"));
    }

    public static class ScanResult {
        private final boolean sensitive;
        private final List<String> detectedRules;
        private final long scanTimeMs;

        public ScanResult(boolean sensitive, List<String> detectedRules, long scanTimeMs) {
            this.sensitive = sensitive;
            this.detectedRules = detectedRules;
            this.scanTimeMs = scanTimeMs;
        }

        public boolean isSensitive() { return sensitive; }
        public List<String> getDetectedRules() { return detectedRules; }
        public long getScanTimeMs() { return scanTimeMs; }
    }

    public ScanResult scanContent(String content) {
        long startTime = System.currentTimeMillis();
        List<String> matches = new ArrayList<>();

        for (Map.Entry<String, Pattern> entry : SENSITIVE_PATTERNS.entrySet()) {
            Matcher matcher = entry.getValue().matcher(content);
            if (matcher.find()) {
                matches.add(entry.getKey());
            }
        }

        long endTime = System.currentTimeMillis();
        return new ScanResult(!matches.isEmpty(), matches, (endTime - startTime));
    }

    public ScanResult scanFile(File file) throws IOException {
        String content = Files.readString(file.toPath());
        return scanContent(content);
    }
}
